def simplifyPath(path):
    """
    . -> curr dir
    .. -> previous/parent dir
    // /// -> /
    others -> valid dir or file name

    rules:
    start with /
    dir within path separated by /
    path not end with / unless root
    path not containing . or ..
    """
    res = ""


path = "/home/"
print(simplifyPath(path))  # /home

path = "/home//foo/"
print(simplifyPath(path))  # /home/foo

path = "/home/user/Documents/../Pictures"
print(simplifyPath(path))  # /home/user/Pictures

path = "/../"
print(simplifyPath(path))  # /

path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))  # /.../b/d
