
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
