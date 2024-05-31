import util
import safeconvert

def handle_response(message) -> str:
    
    p_message = message.lower()
    m = p_message

    print("(debug @ responses.py): " + m)

    if(m) == ("hello"):
        return "hey there!"
    if(m) == ("yo"):
        return "wazzup"
    if(m) == ("roll"):
        return safeconvert.convert(util.roll_6die(), str)
    else:
        return None 

        
if __name__ == "__main__":
    print(handle_response("hello"))
