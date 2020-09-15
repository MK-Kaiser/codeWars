# Two to One
def longest(s1, s2):
    newstring = s1 + s2
    result = set(newstring)
    return ''.join(sorted(result))
    
    
    
Test.describe("longest")
Test.it("Basic tests")
Test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
Test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
Test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy") 
