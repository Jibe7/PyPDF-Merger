# Sciter
## Reactor
Natively supports JSX syntax
Have a virtual dom + a real dom

JSX syntax is as in React, we can use function based components (identical) as well as class based components. Class based components have more functionalities :
```
class MyComponent extends Element {
    let date = new Date();

    constructor() {
        // call super method ...
    }

    ComponentDidMount() { // ... called once the component is mounted in the real DOM }

    ComponentUnmount() { // ... you guessed it }

    ComponentUpdate() { // to update the state of the component : if we want to change a component's property and for that change to be displayed we need to use that function }

    render() {
        return <div>...</div>
    }    
}

To mount to the real DOM we use .patch or <reactor>

It has a window API https://docs.sciter.com/docs/DOM/Window



```

Appeler un script Python avec sciter :
```
import sciter
import subprocess

class Frame(sciter.Window):
    def __init__(self):
        super().__init__()
        self.set_dispatcher(self)

    def run_python_script(self):
        result = subprocess.run(['python', 'your_script.py'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Script Output: {result.stdout}")
        else:
            print(f"Script Error: {result.stderr}")

if __name__ == "__main__":
    frame = Frame()
    frame.load_file("index.html")
    frame.run_app()
```

HTM : 
```
<!DOCTYPE html>
<html>
<head>
    <title>PySciter Example</title>
    <script type="text/tiscript">
        function runPythonScript() {
            view.call('run_python_script', []);
        }
    </script>
</head>
<body>
    <button onclick="runPythonScript()">Run Python Script</button>
</body>
</html>
```