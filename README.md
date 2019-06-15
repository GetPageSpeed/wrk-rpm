# Build latest [wrk](https://github.com/wg/wrk) for CentOS / RedHat 6, 7 and Fedora 27+

|CI|Purpose|Status|
|---|---|---|
|Travis|Tests complete buildability (runs on pull requests, etc.)|[![Build Status](https://travis-ci.org/apache/incubator-pagespeed-mod.svg?branch=master)](https://travis-ci.org/apache/incubator-pagespeed-mod)|
| Copr | Builds `wrk` for CentOS and Fedora (slow repo, but many distros supported)| [<img src="https://copr.fedorainfracloud.org/coprs/getpagespeed/wrk/package/wrk/status_image/last_build.png">](https://copr.fedorainfracloud.org/coprs/getpagespeed/wrk/package/wrk/)  |
| CircleCI | Builds `wrk` for [GetPageSpeed repository](https://www.getpagespeed.com/redhat) (fast CDN repo, RHEL 6 and 7) | [![CircleCI](https://circleci.com/gh/GetPageSpeed/wrk-rpm.svg?style=svg)](https://circleci.com/gh/GetPageSpeed/wrk-rpm) |

If you use CentOS / RHEL, it is highly recommended to install `wrk` from GetPageSpeed repository:

    yum install https://extras.getpagespeed.com/release-el7-latest.rpm
    yum install wrk
