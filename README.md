## Requirements

- [Textual](https://github.com/Textualize/textual)
- Python

## Installation
Clone the repository:
```bash
git clone https://github.com/RchrdAriza/TerminalMarkdown
# Enter the folder
cd TerminalMarkdown
```

Install the requirements using `pip install -r requirements.txt` or simply `pip install textual`.

## Forms of use

To use it you must run the Python script along with the path to the Markdown file

```shell
# for example
python md.py [Mardown_file_here]
```

## Global setup

If you use the script in the above way the Markdown file and the Python file would have to be in the same directory, which would be a bit annoying, wouldn't it?
That's why there is an option to use the Python file from anywhere on the system, which is this:

````bash
# Grant permissions to the file
chmod +x md.py

# Move it to the ```/usr/bin``` folder
sudo mv md.py /usr/bin
````

if you are worried about granting permissions to the Python script you can check all the code [here](https://github.com/RchrdAriza/TerminalMarkdown/blob/main/md.py).

To use it after that just use `md.py`.

```bash
# for example
# In any directory
md.py [path_to_Markdown_file]
```

## Gallery

 <p align="Center">
   <img src="https://res.cloudinary.com/dhqo7n9gd/image/upload/v1696716882/Md/IMG_20231007_170806_111_a3uqg8.jpg" width=350>
   <img src="https://res.cloudinary.com/dhqo7n9gd/image/upload/v1696716883/Md/IMG_20231007_170806_519_zxzqhh.jpg" width=350 >
   <img src="https://res.cloudinary.com/dhqo7n9gd/image/upload/v1696716910/Md/Screenshot_20231007-163717_Termux_jsywjt.jpg" width=250 >
   <img src="https://res.cloudinary.com/dhqo7n9gd/image/upload/v1696717172/Md/Screenshot_20231007-171608_Termux_aiz4ea.jpg" width=250 >
  </p>
