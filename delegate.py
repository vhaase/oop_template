
class DelegateExample:
    def __init__(self):
        self._delegate = None

    def set_delegate(self, delegate_function):
        if callable(delegate_function):
            self._delegate = delegate_function
        else:
            raise ValueError("Delegate must be a callable function")

    def invoke_delegate(self, *args, **kwargs):
        if self._delegate is not None:
            return self._delegate(*args, **kwargs)
        else:
            raise ValueError("No delegate set")

def delegate_function(parameter):
    return f"Delegate invoked with parameter: {parameter}"

# Create an instance of DelegateExample
example = DelegateExample()

# Set the delegate function
example.set_delegate(delegate_function)

# Invoke the delegate
result = example.invoke_delegate("Hello, delegate!")
print(result)