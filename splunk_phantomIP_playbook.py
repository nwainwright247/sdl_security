def block_ip(container):
    ip = phantom.collect2(container, "artifact:*cef.sourceAddress")[0][0]
    phantom.comment(container, f"Blocking mailicious IP: {ip}")
    phantom.act("block ip", parameters=[{"ip":ip, "device":"firewall"}])