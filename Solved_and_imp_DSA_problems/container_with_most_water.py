
# here we solve container with most water problem using two pointer approach -
# time complexity - O(n)
# space complexity - O(1)

def maxArea(height):
    max_water = 0
    lp = 0
    rp = len(height)-1

    while(lp < rp):

        w = rp - lp
        h = min(height[rp], height[lp])
        curr_water = w*h

        max_water = max(max_water, curr_water)

        if height[lp] < height[rp]:
            lp+=1
        else:
            rp-=1

    return max_water

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))


# solve this problem using brute force approach -
# time complexity - O(n^2)
# space complexity - O(1)

def maxArea(height):
        n = len(height)
        max_water = 0

        for i in range(n+1):
            for j in range(i+1, n):
                
                w = j - i
                h = min(height[i], height[j])
                curr_water = w*h

            max_water = max(max_water, curr_water)

        return max_water
    
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))


# solve this problem once again using pointer approach -



        