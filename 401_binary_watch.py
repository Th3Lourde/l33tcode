'''
Ok so we are telling time with a binary watch
4 LEDs on the top, 6 LEDs on the bottom.

Given n ∈ Ζ⁺, where n is the number of LEDs on,
return all of the possible times the watch could
represent.

One way to think about the problem:
We have an array, which represents all of the different
LEDs.

[0,0,0,0,0,0,0,0,0,0]

Given n, we wish to iterate through all of the different
ways where we could perform n choose k.

Where for each possible outcome, we log the time.

So one function to iterate through all of the different
lights that could be on, another function to mapp the lights
that are on to the time that they represent.

Ok, so how can we iterate through all of the different ways
we can do n choose k?

One way I can think of it is by doing a recursive function.

When looping through the different lights, we could have two
parameters: n, lights.

n is the number of lights left for us to light.
lights is the current lights that are activated.
This approach will cause us to sometimes come to
the same light configuration multiple times.

We would probably want to keep track of what configurations we
have already seen and what configurations we haven't seen yet.

How to do this?

One way to tell whether or not we have a certain configuration
or whether or not an element is already in our configuration is
to use a set.

However, since we can just index the value, if we use a list we
will still have constant look-up time.

So let's just use a list instead.

Let lights be [0,0,0,0,0,0,0,0,0,0] ← Have these be strings

For every call or recurse, loop through
lights, set one of the zeros to be ones,
call the function again.

Keep a set of the times that we already have.
Also keep a list of the times that we will be
returning.

The conversion is pretty fast, so nvm.

ans = []
times = ()

def recurse(n, lights):
    if n == 0:
        # lights is a list
        time = l_to_t(lights)

        if time not in times:
            times.add(time)
            ans.append(time)

    elif n > 0:
        for i in range(len(lights)):
            if lights[i] == "0":
                tmp = list(lights)
                tmp[i] = "1"
                recurse(n-1, tmp)


Ok so I'm feeling pretty good for iterating,
time for us to create the list --> str, which
represents the time being shown.

So the first four digits reprsent the hour
The second 6 digits reprsent the minute

Split the list, create a binary, bin --> int --> str ?
Sounds good to me.

Ok so here's how we go from bin to str:
    str = str(int("binaryNum", 2))

    e.g. : str(int('0011', 2)) --> '3'

Ok so do one for the lhs, one for the rhs.

def l_to_t(lights):
    hr = lights[:5]
    min = lights[5:]

    return str(int(hr, 2)) + ":" + str(int(min, 2))

def l_to_t(lights):
    hr = lights[:5]
    min = lights[5:]

    hr = "".join(hr)
    min = "".join(min)

    min = str(int(min, 2))

    if len(min) == 1:
        min = "0" + min

    return str(int(hr, 2)) + ":" + min


'''

class Solution:
    def readBinaryWatch(self, num):

        def l_to_t(lights):
            hr = lights[:4]
            min = lights[4:]

            hr = "".join(hr)
            min = "".join(min)

            min = str(int(min, 2))

            if len(min) == 1:
                min = "0" + min

            hr = int(hr, 2)

            if hr > 11:
                return None

            return str(hr) + ":" + min

        ans = []
        times = set({None})

        def recurse(n, lights):
            if n == 0:
                # lights is a list
                time = l_to_t(lights)

                print(time)

                if time not in times:
                    times.add(time)
                    ans.append(time)

            elif n > 0:
                for i in range(len(lights)):
                    if lights[i] == "0":
                        tmp = list(lights)
                        tmp[i] = "1"
                        recurse(n-1, tmp)

        recurse(num, ["0","0","0","0","0","0","0","0","0","0"])

        return ans


def l_to_t(lights):
    hr = lights[:4]
    min = lights[4:]

    hr = "".join(hr)
    min = "".join(min)

    min = str(int(min, 2))

    if len(min) == 1:
        min = "0" + min

    # return min + ":" + str(int(hr, 2)
    # return str(int(min, 2)) + ":" + hr
    return str(int(hr, 2)) + ":" + min


l_to_t(["1","1","0","0","0","0","0","0","0","0"])


if __name__ == '__main__':
    s = Solution()

    print(s.readBinaryWatch(2))
