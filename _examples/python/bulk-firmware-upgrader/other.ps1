#$firmware_name = "tna-30x-1.12.0-r54564-20240808-tn-110-prs-squashfs-sysupgrade.bin"
<#
$serverScript = {
    Set-Location "$env:USERPROFILE\Nextcloud\Ridgetop Shared\configs\firmware\60GHz-Tach\"
    python3 -m http.server 8000 --bind 0.0.0.0
}

$job = Start-Job -ScriptBlock $serverScript

$ipAddress = Get-NetIPAddress |
    Where-Object { 
        $_.AddressFamily -eq 'IPv4' -and 
        $_.IPAddress -like '192.168.75.*' -and 
        $_.PrefixLength -eq 24 
    } |
    Select-Object -First 1 -ExpandProperty IPAddress

Write-Output "Your IP: $ipAddress"
#>

#Stop-Job $job