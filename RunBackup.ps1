$backupFolder = "C:\Users\$env:UserName\AppData\LocalLow\IronGate"
$worldsLocation = "C:\Users\$env:UserName\AppData\LocalLow\IronGate\Valheim\worlds"
$charactersLocation = "C:\Users\$env:UserName\AppData\LocalLow\IronGate\Valheim\characters"

Write-Host "Checking for folders."
If (!(Test-Path "$backupFolder\ValheimBackups")){
New-Item -Path "$backupFolder" -Name "ValheimBackups" -ItemType Directory
Write-Host "Created folder."
}ELSE{
Write-Host "$backupFolder\ValheimBackups already exists."
}

$backupFolder = "C:\Users\$env:UserName\AppData\LocalLow\IronGate\ValheimBackups"
If (!(Test-Path "$backupFolder\worlds")){
New-Item -Path "$backupFolder" -Name "worlds" -ItemType Directory
Write-Host "Created folder."
}ELSE{
Write-Host "$backupFolder\worlds already exists."
}
If (!(Test-Path "$backupFolder\characters")){
New-Item -Path "$backupFolder" -Name "characters" -ItemType Directory
Write-Host "Created folder."
}ELSE{
Write-Host "$backupFolder\characters already exists."
}

$date = (Get-Date -Format yyMMdd.HHmm)
Write-Host "Date: $date"

Compress-Archive -path "$worldsLocation" -destinationpath $BackupFolder\worlds\$date.zip -Update
Compress-Archive -path "$charactersLocation" -destinationpath $BackupFolder\characters\$date.zip -Update


Read-Host -Prompt "Backup complete. Press Enter to exit"
exit