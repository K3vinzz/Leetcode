class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        canonicalPath = "/"
        for dir in split_path:
            # print(stack)
            if dir == "" or dir == ".":
                pass
            elif dir == ".." and stack:
                stack.pop()
            elif dir == ".." and not stack:
                pass
            else:
                stack.append(dir)

        while stack:
            canonicalPath += f"{stack.pop(0)}/"

        canonicalPath = canonicalPath.rstrip("/")
        if canonicalPath == "":
            return "/"
        return canonicalPath

s = Solution()
print(s.simplifyPath("/../"))

