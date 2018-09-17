[![Build Status](https://travis-ci.org/romanchyla/arxiv_biboverlay.svg)](https://travis-ci.org/romanchyla/arxiv_biboverlay)
[![Coverage Status](https://coveralls.io/repos/romanchyla/arxiv_biboverlay/badge.svg)](https://coveralls.io/r/romanchyla/arxiv_biboverlay)

# arxiv_biboverlay
Tiny microservice to help arxiv. It provides a bootstrap service to obtain 
OAuth token that are subordinate to the main Arxiv OAuth client.

## deployment 
    
    TODO: use dockerfile
    
## Usage:

    `curl somewhere.com/token`
    
    The output will contain a new OAuth token. If we provide also a cookie, the 
    same token will be returned (without creating a new one).
