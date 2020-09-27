#!/usr/bin/env bash
cd /home
date -u >> /var/log/home_usage_by_user.log
for i in *
do
  du -ha -d 0 $i >> /var/log/home_usage_by_user.log
done
