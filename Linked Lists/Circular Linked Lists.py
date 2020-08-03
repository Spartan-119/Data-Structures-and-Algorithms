#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicing CIRCULAR LINKED LISTS

יְהוָ֖ה אִ֣ישׁ מִלְחָמָ֑ה יְהוָ֖ה שְׁמֽוֹ׃

Created on Tue Aug  4 01:27:02 2020

@author: abin
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    
    def __init__(self):
        self.head = None
    
    