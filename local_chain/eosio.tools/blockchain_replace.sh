#!/bin/bash
find ./ -type f -readable -writable -exec sed -i "s/eosio/new_name/g" {} \;
find ./ -type f -readable -writable -exec sed -i "s/Eosio/New_name/g" {} \;
find ./ -type f -readable -writable -exec sed -i "s/EOSIO/NEW_NAME/g" {} \;
find ./ -execdir rename 's/eosio/new_name/' '{}' \+;
find ./ -execdir rename 's/Eosio/New_name/' '{}' \+;
find ./ -execdir rename 's/EOSIO/NEW_NAME/' '{}' \+;

find ./ -type f -readable -writable -exec sed -i "s/eos/new_short_name/g" {} \;
find ./ -type f -readable -writable -exec sed -i "s/Eos/New_short_name/g" {} \;
find ./ -type f -readable -writable -exec sed -i "s/EOS/NEW_SHORT_NAME/g" {} \;
find ./ -execdir rename 's/eos/new_short_name/' '{}' \+;
find ./ -execdir rename 's/Eos/New_short_name/' '{}' \+;
find ./ -execdir rename 's/EOS/NEW_SHORT_NAME/' '{}' \+;