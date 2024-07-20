class Log():
    DEBUG_ENABLED = False
    
    def d(output: str):
        '''
        Log the given output string to stdout if debug flag at the top
        of this class is enabled
        
        Parameters:
            output (str): The string to log
        '''
        if Log.DEBUG_ENABLED:
            print(output)