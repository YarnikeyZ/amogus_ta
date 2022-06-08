from subprocess import getoutput as gout
clear = gout("clear")
print(clear)
w = "\033[48;5;255m\033[38;5;255m"
b = "\033[48;5;232m\033[38;5;232m"
r = "\033[48;5;196m\033[38;5;196m"
rr = "\033[48;5;160m\033[38;5;160m"
lb = "\033[48;5;45m\033[38;5;45m"
db = "\033[48;5;32m\033[38;5;32m"
c = "\033[0;0m"
print(f'''
{w}                                                      
{w}               {b}____________________{w}                   
{w}              {b}/ __________________ \\{w}                  
{w}             {b}/ /{r}                  {b}\\ \\{w}                 
{w}            {b}/ /{r}                    {b}\\ \\{w}                
{w}           {b}/ /{r}           ___________{b}\\ \\{w}___            
{w}          {b}| |{rr}|{r}          {b}/ _______________{b} \\{w}           
{w}          {b}| |{rr} |{r}        {b}/ /{lb}     _______   {b}\\ \\{w}          
{w}    ______{b}| |{rr} |{r}       {b}/ /{db}\\{lb}     {w}\\______\\{lb}   {b}\\ \\{w}         
{w}   {b}/ _____  |{rr} |{r}       {b}| |{db} \\{lb}______________/{b}| |{w}         
{w}  {b}| |{r}     {b}| |{rr} |{r}       {b}\\ \\{db}                 {b}/ /{w}         
{w}  {b}| |{r}     {b}| |{rr}  |{r}       {b}\\ \\{db}_______________{b}/ /{w}          
{w}  {b}| |{rr}\\{r}___{rr}/{b}| |{rr}  |{r}        {b}\\____________   __/{w}           
{w}  {b}| |{rr}     {b}| |{rr}   |{r}                   {rr}/{b}| |{w}              
{w}  {b}| |{rr}     {b}| |{rr}   |{r}                  {rr}| {b}| |{w}              
{w}  {b}| |{rr}     {b}| |{rr}    |{r}                 {rr}| {b}| |{w}              
{w}  {b}| |{rr}     {b}| |{rr}    |{r}                {rr}|  {b}| |{w}              
{w}  {b}| |{rr}     {b}| |{rr}     \\{r}______________{rr}/   {b}| |{w}              
{w}  {b}| |{rr}     {b}| |{rr}                        {b}| |{w}              
{w}  {b}| |{rr}_____{b}| |{rr}         ________       {b}| |{w}              
{w}   {b}\\______  |{rr}        {b}/ ______ \\{rr}      {b}| |{w}              
{w}          {b}| |{rr}       {b}| |{w}      {b}| |{rr}     {b}| |{w}              
{w}          {b}| |{rr}       {b}| |{w}      {b}| |{rr}     {b}| |{w}              
{w}          {b}| |{rr}       {b}| |{w}      {b}| |{rr}     {b}| |{w}              
{w}          {b}| |{rr}      {b}/ /{w}       {b}\\ \\{rr}_____{b}/ /{w}              
{w}          {b}\\ \\{rr}_____{b}/ /{w}         {b}\\_______/{w}               
{w}           {b}\\_______/{w}                                  
{w}                                                      
{c}

Traceback (most recent call last):
  File "amogus.py", line 1, in <module>
    print(sys.argv[0])
NameError: name 'sys' is not defined. Did you mean: 'sus'?''')
input()
print(clear)
