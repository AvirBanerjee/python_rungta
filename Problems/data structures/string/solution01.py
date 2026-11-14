def sort(str):
    result=""
    for ch in "0123456789":
        if ch not in str:
            result+=ch
    for ch in "abcdefghijklmnopqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in str:
            result+=ch      
    return result            

value="4648nfjr7dnr8fnf8dns"

print(sort(value))