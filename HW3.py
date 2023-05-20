import copy

class Page_replacement :

    def __init__( self ) :

        self.frame_num = 0 
        self.pages = []
        self.output_file = 0
        self.method = 0

    def Read_input( self ) :
        
        file_name = str( input( "Please input the file name : \n" ) )
        input_file = open( file_name + ".txt", "r" )
        self.output_file = open( "out_" + file_name + ".txt", "w" )

        self.method, self.frame_num = input_file.readline().split()
        self.pages = [ x for x in str( input_file.readline() ) if x >= "0" and x <= "9" ]

        if self.method == "1" :
            self.FIFO()
        elif self.method == "2" :
            self.LRU()
        elif self.method == "3" :
            self.LFU_LRU()
        elif self.method == "4" :
            self.MFU_FIFO()
        elif self.method == "5" :
            self.MFU_LRU()
        elif self.method == "6" :
            self.FIFO(), self.LRU(), self.LFU_LRU(), self.MFU_FIFO(), self.MFU_LRU()
        else :
            print( "There is no such method" )

        input_file.close()
        self.output_file.close()

    def FIFO( self ) :

        stack, is_fault, fault_num, replace_num = [], False, 0, 0
        new_data = copy.deepcopy( self.pages )

        self.output_file.write( "--------------FIFO-----------------------\n" )

        while new_data :

            cur = new_data.pop( 0 )
            ans_str = cur + "\t"

            if stack and cur in stack :
                pass 

            elif len( stack ) == int( self.frame_num ) :
                stack.pop( 0 )
                stack.append( cur )

                is_fault, fault_num, replace_num = True, fault_num + 1, replace_num + 1

            elif len( stack ) < int( self.frame_num ) :
                stack.append( cur ) 

                is_fault, fault_num = True, fault_num + 1

            ans_str, is_fault = self.Out_str( stack, ans_str, is_fault )
            self.output_file.write( ans_str + "\n" )

        self.output_file.write( "Page Fault = " + str( fault_num ) + "  Page Replaces = " + str( replace_num ) + "  Page Frames = " + str( self.frame_num ) + "\n\n" )

    def LRU( self ) :

        stack, is_fault, fault_num, replace_num = [], False, 0, 0
        new_data = copy.deepcopy( self.pages )

        self.output_file.write( "--------------LRU-----------------------\n" )

        while new_data :

            cur = new_data.pop( 0 )
            ans_str = cur + "\t"

            if stack and cur in stack :
                stack.remove( cur )
                stack.append( cur ) 

            elif len( stack ) == int( self.frame_num ) :
                stack.pop( 0 )
                stack.append( cur )

                is_fault, fault_num, replace_num = True, fault_num + 1, replace_num + 1

            elif len( stack ) < int( self.frame_num ) :
                stack.append( cur ) 

                is_fault, fault_num = True, fault_num + 1

            ans_str, is_fault = self.Out_str( stack, ans_str, is_fault )
            self.output_file.write( ans_str + "\n" )

        self.output_file.write( "Page Fault = " + str( fault_num ) + "  Page Replaces = " + str( replace_num ) + "  Page Frames = " + str( self.frame_num ) + "\n\n" )

    def LFU_LRU( self ) :

        stack, is_fault, fault_num, replace_num = {}, False, 0, 0
        new_data = copy.deepcopy( self.pages )

        self.output_file.write( "--------------Least Frequently Used LRU Page Replacement-----------------------\n" )

        while new_data :

            cur = new_data.pop( 0 )
            ans_str = cur + "\t"

            if stack and cur in stack :
                temp_counter = stack[cur]
                del stack[cur]
                stack[cur] = temp_counter + 1

            elif len( stack ) == int( self.frame_num ) :
                victim = min( stack, key=stack.get )
                del stack[victim]
                stack[cur] = 0

                is_fault, fault_num, replace_num = True, fault_num + 1, replace_num + 1

            elif len( stack ) < int( self.frame_num ) :
                stack[cur] = 0

                is_fault, fault_num = True, fault_num + 1 

            key_list = [ x for x in stack.keys() ]
            ans_str, is_fault = self.Out_str( key_list, ans_str, is_fault )
            self.output_file.write( ans_str + "\n" )

        self.output_file.write( "Page Fault = " + str( fault_num ) + "  Page Replaces = " + str( replace_num ) + "  Page Frames = " + str( self.frame_num ) + "\n\n" )

    def MFU_FIFO( self ) :

        stack, is_fault, fault_num, replace_num = {}, False, 0, 0
        new_data = copy.deepcopy( self.pages )

        self.output_file.write( "--------------Most Frequently Used Page Replacement -----------------------\n" )

        while new_data :

            cur = new_data.pop( 0 )
            ans_str = cur + "\t"

            if stack and cur in stack :
                stack[cur] += 1

            elif len( stack ) == int( self.frame_num ) :
                victim = max( stack, key=stack.get )
                del stack[victim]
                stack[cur] = 0
                
                is_fault, fault_num, replace_num = True, fault_num + 1, replace_num + 1

            elif len( stack ) < int( self.frame_num ) :
                stack[cur] = 0

                is_fault, fault_num = True, fault_num + 1

            key_list = [ x for x in stack.keys() ]
            ans_str, is_fault = self.Out_str( key_list, ans_str, is_fault )
            self.output_file.write( ans_str + "\n" )

        self.output_file.write( "Page Fault = " + str( fault_num ) + "  Page Replaces = " + str( replace_num ) + "  Page Frames = " + str( self.frame_num ) + "\n\n" )

    def MFU_LRU( self ) :

        stack, is_fault, fault_num, replace_num = {}, False, 0, 0
        new_data = copy.deepcopy( self.pages )

        self.output_file.write( "--------------Most Frequently Used LRU Page Replacement -----------------------\n" )

        while new_data :

            cur = new_data.pop( 0 )
            ans_str = cur + "\t"

            if stack and cur in stack :
                temp_counter = stack[cur]
                del stack[cur]
                stack[cur] = temp_counter + 1

            elif len( stack ) == int( self.frame_num ) :
                victim = max( stack, key=stack.get )
                del stack[victim]
                stack[cur] = 0

                is_fault, fault_num, replace_num = True, fault_num + 1, replace_num + 1

            elif len( stack ) < int( self.frame_num ) :
                stack[cur] = 0

                is_fault, fault_num = True, fault_num + 1

            key_list = [ x for x in stack.keys() ]
            ans_str, is_fault = self.Out_str( key_list, ans_str, is_fault )
            self.output_file.write( ans_str + "\n" )

        self.output_file.write( "Page Fault = " + str( fault_num ) + "  Page Replaces = " + str( replace_num ) + "  Page Frames = " + str( self.frame_num ) + "\n" )

    def Out_str( self, stack, ans_str, is_fault ) :

        for x in reversed( stack ) :
                ans_str += x

        if is_fault :
                ans_str += "\tF"
                is_fault = False
        
        return ans_str, is_fault

test = Page_replacement()
test.Read_input()