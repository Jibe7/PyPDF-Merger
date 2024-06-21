import sciter
import subprocess

class Frame(sciter.Window):

    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=False)
        self.set_dispatch_options(enable=True, require_attribute=False)
        pass

     #@sciter.script - optional attribute here because of self.set_dispatch_options()
    def kkk(self):
        print("kkk called!")
        return "hello"

    def run_python_script(self):
        print("Called")
        result = subprocess.run(['python example.py'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Script Output: {result.stdout}")
        else:
            print(f"Script Error: {result.stderr}")

if __name__ == "__main__":
    frame = sciter.Window(ismain=True, uni_theme=True)
    frame.load_file("pyrunner.htm")
    frame.expand()
    frame.run_app()
