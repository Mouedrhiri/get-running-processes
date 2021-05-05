# Get Running Processes By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

`from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

`from time import sleep`

### The I Used The Library Imaplib To Give Me Acces To Gmail Account

`import imaplib`

### I've Made a Function For The Progress Bar Like That :

    def progress(rang):
    for i in tqdm(rang, desc ="Progress : "):
            sleep(.1)

> As You All Can See I Made This Progress Bar Relative To The Searching Progress

---

# Let's Begin The Code Explanation :

## I've Used Here WMI library to get all the processes

> `import wmi`

## I've Created One List To Stock The Running Process :

    l = []

## I Must iterate Over The Processes :

    for process in f.Win32_Process():

> Add It To The Empty List To Use it In The Progress Bar

        l.append(process.ProcessId)

## Now We Will Iterate Over The Processes IDs And Names :

    for process in f.Win32_Process():

> And Each Time We Will Print The ID and The Process Name

     print(f"{process.ProcessId:<10} {process.Name}")

---

Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)
