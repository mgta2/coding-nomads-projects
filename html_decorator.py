# Project HTML Element Decorator:
# Write a decorator function that wraps text passed to it in a specified HTML tag.
# The user should be able to decide which tag to use.

def tagify(html):
    def decorator(initial_func):
        def wrapper(*args, **kwargs):
            return f"<{html}>" + initial_func(*args, **kwargs) + f"</{html}>"
        return wrapper
    return decorator

@tagify("div")
def my_text():
    return "This text needs to become suitable for a website."

print(my_text())  # OUTPUT: <div>This text needs to become suitable for a website.</div>

@tagify("p")
def greet(name):
    return f"Hello, {name}"

print(greet("Bessy"))  # OUTPUT: <p>Hello, Bessy</p>