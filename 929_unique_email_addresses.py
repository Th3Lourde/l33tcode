'''
Given a list of emails.
If we send an email to each address,
how many unique addresses actually
receive mail?

Basic stuff:
  The domain can make something unique
  th3.lourde is the same as th3lourde


Have a dict of emails that we have seen.

When you see a ., remove the '.' and add
the result to the dict (or check that it exists).

After +, the local name is gone.

Ok so we want to count the number of unique emails
that we have.

Step through each email, break on the '@' symbol.

Get the local name, get the domain,
create a new email, if we don't have it, add to dict.

How to get local:
remove all '.', if we see a '+' stop.


How to get domain:
just get the second element in the list.

return the length of our keys

["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

"test.email+alex@leetcode.com"

local: "testemail" <-- start with "", for i in range, if + break, if not ., append to string
domain = "leetcode.com"

end = "testemail@leetcode.com"

d = ("testemail@leetcode.com" )

Just use a set, since we don't actually need a key.

"test.e.mail+bob.cathy@leetcode.com"
local: "testemail"
domain: "leetcode.com"

"testemail@leetcode.com" \in d, continue.


continue this way, return len(d)

Assuming that we are given valid emails? <-- correct assumption

How could we make this quicker?

Have redirects? But we'd still need to know what we are re-directing to.

'''

class Solution:
    def numUniqueEmails(self, emails):
        s = set()

        for email in emails:
            tmp = email.split("@")


            # Get local
            local = ""
            for c in tmp[0]:
                if c == "+":
                    break

                elif c != ".":
                    local = local + c

            # Domain is always tmp[1]

            sig = local + "@" + tmp[1]

            if sig not in s:
                s.add(sig)

        return len(s)


if __name__ == '__main__':
    s = Solution()

    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
