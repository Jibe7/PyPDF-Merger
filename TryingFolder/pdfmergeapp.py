import sciter

if __name__ == "__main__":
    frame = sciter.Window(ismain=False, uni_theme=True)
    frame.load_file("pdfmergeapp.htm")
    frame.expand()
    frame.run_app()