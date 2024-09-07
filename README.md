    
     █████╗ ████████╗████████╗███████╗   ███╗   ███╗   ██████╗ ████████╗███████╗  
    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝   ████╗ ████║   ██╔══██╗╚══██╔══╝██╔════╝  
    ███████║   ██║      ██║   █████╗     ██╔████╔██║   ██████╔╝   ██║   ███████╗  
    ██╔══██║   ██║      ██║   ██╔══╝     ██║╚██╔╝██║   ██╔═══╝    ██║   ╚════██║  
    ██║  ██║██╗██║██╗   ██║██╗███████╗██╗██║ ╚═╝ ██║██╗██║██╗     ██║██╗███████║██╗  
    ╚═╝  ╚═╝╚═╝╚═╝╚═╝   ╚═╝╚═╝╚══════╝╚═╝╚═╝     ╚═╝╚═╝╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚═╝    


# 𝗔dd 𝗧imestamps 𝗧o 𝗘ach one of 𝗠y 𝗣rint statemen𝗧𝗦

A very simple yet customizable package to add timestamps to your print statements.

You can replace the default 'print()', keeping all of its default options, or use the built-in "printt()" command, that accepts all the same arguments as "print()"


## Installation

To install, run

```bash
  pip install attempts
```

## Usage

Import and initialize. The only required parameter is 'replace_print'. 

```bash
  import attempts

  attempts.init(replace_print=False)  # By default, it does not replace the original "print()", so you have to use "printt()".
  # or
  attempts.init(replace_print=True) 

```



## Demo

Insert gif or link to demo


## FAQ


#### Question 1

Answer 1

#### Question 2

Answer 2

## TO-DO
- Add option to replace default print or use "printt" command.
- Add option to choose timestamp color
- Add option to benchmark using a key and output time delta
- Add option to store timestamps in memory, given a variable limit, to optmize memory usage
- Add option to output a formatted table with outputs 
    
## License

[MIT](https://choosealicense.com/licenses/mit/)

