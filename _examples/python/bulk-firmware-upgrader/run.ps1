$firmware_url = "https://tachyon-networks.com/fw/tna-30x/1.12.0/tna-30x-1.12.0-r54573-20240904-tn-110-prs-squashfs-sysupgrade.bin"

python3 firmware_upgrade.py -u root -p admin -f $firmware_url -if ips.txt

