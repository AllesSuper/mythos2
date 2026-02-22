param(
  [Parameter(Position=0)]
  [string]$Command = "help",

  [Parameter(ValueFromRemainingArguments=$true)]
  [string[]]$Args
)

python .\mythos_cli.py $Command @Args