#!/usr/bin/env ruby
puts ARGV.map{|p|Dir[p].map{|f|File.realpath(f)}}