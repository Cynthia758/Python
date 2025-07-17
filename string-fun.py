c = "Vaidehi"
print(len(c))
print(max(c))
print(min(c))
print(sorted(c))
print(sorted(c,reverse=True))
print(sorted(c,reverse=False))
# Functions which are only applicable to strings...
# 1. Capitalize/Title/Upper/Lower/Swapcase
text = "it iS RAINING todayy"
print(text.capitalize());
print(text.title());
print(text.upper());
print(text.lower());

p = 'VAIDEHI';
q = 'vaidehi';
print(p.swapcase());
print(q.swapcase());
print(text.swapcase());

# 2. Count
# Case-sensitivee...
print(text.count('i'));
print(text.count('ing'));
print(text.count('I'));
