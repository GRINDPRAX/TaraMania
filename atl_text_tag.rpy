transform bounce:
    ease 0.5 yoffset 10 matrixcolor TintMatrix("#f00")
    ease 0.5 yoffset -10 matrixcolor TintMatrix("#00f")
    repeat
transform bounce_text(yoff):
    ease 0.5 ypos yoff
    ease 0.5 ypos -yoff
    repeat
transform rotate_text(speed):
    linear speed rotate 180
    linear speed rotate 360
    rotate 0
    repeat
transform drop_text(letter, time):
    contains:
        letter
    contains:
        letter
        yoffset 0 alpha 1
        easeout_circ time yoffset 50 alpha 0
        letter
        repeat
transform fade_in_text(time=0.5, distance=20):
    alpha 0 xoffset distance
    ease time alpha 1 xoffset 0


transform text_rotate_3d(time=1.5):
    matrixanchor (0.5,0.5)
    matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    linear time matrixtransform RotateMatrix(180,0,0) * OffsetMatrix(0,0,100)
    linear time matrixtransform RotateMatrix(360,0,0) * OffsetMatrix(0,0,100)
    matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,100)
    repeat

init python:
    class ATLText(renpy.Displayable):
        def __init__(self, child, transforms, offset=0, hold=False,**kwargs):
            super(ATLText, self).__init__(**kwargs)
            self.child = At(child, *transforms)
            self.offset = offset
            self.hold = hold

            child_render = renpy.render(child, 0, 0, 0, 0)
            self.width, self.height = child_render.get_size()

            if config.atl_start_on_show:
                renpy.render(self.child, 0, 0, 0, 0)

        def render(self, width, height, st, at):
            # Apply the time offset.
            st = st + self.offset
            at = at + self.offset
            if self.hold:
                st = max(st, 0)
                at = max(at, 0)

            # Get child render and our output render
            child_render = renpy.render(self.child, width, height, st, at)
            # self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Next section is to figure out the offset applied to the blit
            # Get_Placement returns a tuple containing:
            # xpos, ypos, xanchor, yanchor, xoffset, yoffset, subpixel
            child_pos = self.child.state.get_placement()
            # Sometimes the output of get_placement has some None values in there.
            # So use this to get safe output.
            def none_to_float(param):
                if param is None:
                    return 0.0
                return param
            child_xpos = none_to_float(child_pos[0]) + none_to_float(child_pos[4])
            child_ypos = none_to_float(child_pos[1]) + none_to_float(child_pos[5])

            render.blit(child_render, (child_xpos,child_ypos))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Allows one to use one or more ATL transforms to define a movement for text.
    # Arguments are separated by ',' and transform parameters are separated by '~'
    # The offset and hold arguments are optional.
    # Arguments:
    #   offset: (float/'#'/'-#') The time offset between two characters (in seconds).
    #                     If #, then it use's the user's cps setting as the offset
    #                     If -#, does the above but treats it as negative.
    #                     See Notes for details on negative offsets
    #   hold: ('#') Tells the displayable to hold the value at 0 if time is negative.
    #               Is ignored if offset is positive.
    #               See Notes on negative offsets for more details.
    #   transform_name: (string) The name of a defined transform.
    #                            Will throw an error if doesn't exist
    #   param: (float/string/'#') A parameter for the transform. Must be ordered by position.
    #     All numbers will be interpreted as floats. Strings should evaluate to a displayable, a global variable OR
    #     optionally, can be left as '#' in order to use the current character as a displayable parameter.
    #     (No current support for keyword args)
    # Notes:
    #   - Transforms are applied using an At() displayable and are added in the same order.
    #
    #   - If a negative offset is supplied, we have to be careful of what time
    #   we supply to the ATL's render function. If we give it a negtive number, it
    #   will treat that value as it's new 0 seconds. So if we feed it -2 seconds
    #   to start, then when it reaches -1.8 seconds, it'll treat that as 0.2 seconds.
    #   This has the effect of syncronizing every letter, which isn't what we want.
    #
    #   - To combat this, if a negative offset is given I instead push the first
    #   letter forward in time. That way each subsequent character can approach
    #   zero with the negative offset.
    #   So, for example, if we have 6 characters and the offset is to be -0.2 seconds,
    #   then the 1st character will start at 1.0 seconds, 2nd will start at 0.8,
    #   and so on until the 6th character starts at 0 seconds.
    #
    #   - However, this may not always be the ideal setup for all transforms,
    #   such as fades. An alternative is then to hold the time at 0 until it becomes
    #   positive. Which is what the 'hold' argument applies.
    #   Re-using the example from before, every character starts at 0 seconds,
    #   The 1st character will start to move immediately, but the 2nd character
    #   will wait 0.2 seconds before starting. The 3rd waits 0.4, 4th waits 0.6,
    #   until the 6th character waits 1.0 seconds before starting.
    #
    # Examples:
    #   {atl=[offset],[hold],[transform_name]~[param]~...),...}Text{/atl}
    #   {atl=0.1, rotate_text~0.5, bounce_text~10}Text{/atl}
    #   {atl=drop_text~#~0.5}Text{/atl}
    #   {atl=-#,#,fade_in_text~1.0~-100}Text{/atl}
    def atl_tag(tag, argument, contents):
        new_list = []
        # Split the argument into a list of transforms and their parameters
        arg_list = argument.split(',')
        atl_list = []
        time_offset = 0
        hold = False
        # Check for an offset

        if arg_list[0] == "#" or arg_list[0] == "-#":
            if preferences.text_cps is not 0:
                time_offset = (1.0 / preferences.text_cps)
                if arg_list[0] == "-#":
                    time_offset = time_offset * -1.0
            arg_list.pop(0)

        else:
            try:
                time_offset = float(arg_list[0])
                arg_list.pop(0)
            except:
                time_offset = 0
        if arg_list[0] == "#":
            hold = True
            arg_list.pop(0)
        # Go through the arguments for transforms.
        # Returns False if it finds a "#" in the params without text set
        # Otherwise returns a list of transforms
        def arg_handler(arg_list, text=None):
            return_list = []
            for arg in arg_list:
                if '~' in arg:
                    txt_param_list = arg.split('~')
                    arg = txt_param_list[0].strip()
                    # Remove the name of the transform from the parameters list
                    txt_param_list.pop(0)
                    param_list = []
                    for i in range(len(txt_param_list)):
                        param = None
                        txt_param_list[i] = txt_param_list[i].strip()
                        # If a #, then we'll have to do some special stuff later
                        if txt_param_list[i] == "#":
                            if text == None: # If we weren't supplied a way to handle this, return
                                return False
                            param_list.append(text)
                            continue
                        # Attempt a float
                        try:
                            param = float(txt_param_list[i])
                        except ValueError:
                            param = None
                        # Attempt a global variable
                        if param == None and txt_param_list[i] in globals():
                            param = globals()[txt_param_list[i]]
                        # Attempt a displayable
                        elif param == None:
                            param = renpy.displayable(txt_param_list[i])
                        param_list.append(param)
                    return_list.append(globals()[arg](*param_list))
                else:
                    arg = arg.strip()
                    return_list.append(globals()[arg])
            return return_list

        # Setup char_index
        char_index = 0
        count_back = False # Used to know if we count forwards or backwards

        if time_offset < 0 and not hold:
            for kind,text in contents:
                if kind == renpy.TEXT_TEXT:
                    char_index += len(text)
                # Handles adding images into text. Remove if you don't want this behavior
                elif kind == renpy.TEXT_TAG:
                    if text.find("image") != -1:
                        char_index += 1
            time_offset = time_offset * -1.0
            count_back = True
        atl_list = arg_handler(arg_list) # Attempt to get a list of atl functions
        # Usual kinetic-text-tag text handling
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    if atl_list == False:

                        new_atl_list = arg_handler(arg_list, char_text)
                        char_disp = ATLText(char_text, new_atl_list, char_index * time_offset, hold)
                    else:
                        char_disp = ATLText(char_text, atl_list, char_index * time_offset, hold)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    if count_back:
                        char_index -= 1
                    else:
                        char_index += 1
            elif kind == renpy.TEXT_TAG:
                # Handles adding images into text. Remove if you don't want this behavior
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    if atl_list == False:
                        new_atl_list = arg_handler(arg_list, my_img)
                        img_disp = ATLText(my_img, new_atl_list, char_index * time_offset, hold)
                    else:
                        img_disp = ATLText(my_img, atl_list, char_index * time_offset, hold)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                    if count_back:
                        char_index -= 1
                    else:
                        char_index += 1
                elif not my_style.add_tags(text):
                        new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["atl"] = atl_tag
