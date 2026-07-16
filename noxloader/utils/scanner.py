def scan_url(url):
    url_lower = url.lower()
    platform = "Universal"
    domain = "Unknown"

    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        platform = "YouTube"
        domain = "youtube.com"
    elif "tiktok.com" in url_lower:
        platform = "TikTok"
        domain = "tiktok.com"
    elif "instagram.com" in url_lower:
        platform = "Instagram"
        domain = "instagram.com"
    elif "facebook.com" in url_lower or "fb.watch" in url_lower or "fb.gg" in url_lower:
        platform = "Facebook"
        domain = "facebook.com"
    elif "twitter.com" in url_lower or "x.com" in url_lower:
        platform = "X"
        domain = "x.com"
    elif "vimeo.com" in url_lower:
        platform = "Vimeo"
        domain = "vimeo.com"
    else:
        try:
            domain = url.split("//")[-1].split("/")[0]
        except:
            domain = "Unknown"

    return {
        "domain": domain,
        "platform": platform
    }
