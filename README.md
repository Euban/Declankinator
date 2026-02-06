# Declankinator - AI / Slop Removal Aggregate

Inspired by [laylavish's repo](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist). Her goal is primary image/video. This fork is just me cobbling together some LLM generated sites and merging from other uBlacklist lists, and converting them into uBLock, pihole, and a base-url agnostic format as well. Can't get 100%, nor perhaps even 0.1% of the slop on the net, but I've noticed the same few sites over a couple months, so maybe there's merit to this...

Inherits sites from the AI/Human slop lists at [SSSS](https://github.com/NotaInutilis/Super-SEO-Spam-Suppressor), [agsimmons/ai-content-blocklist](https://github.com/agsimmons/ai-content-blocklist), [wdmpa/content-farm-list](https://github.com/wdmpa/content-farm-list), as well as slop from [popcar2/BadWebsiteBlocklist](https://github.com/popcar2/BadWebsiteBlocklist) but using the handy script converts those links into ublock filters as well.

The goal is to pull from these lists, and convert rules back into raw URLs, so that anyone can convert them to uBlacklist, uBlock, pihole, or some other format, as shown with the python scripts. 

### This is mostly experimental, and above all else, the result of me throwing random ideas together. so it's ain't... all that.
