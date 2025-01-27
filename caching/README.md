# Caching



## Background Context

In this project, you will learn about different caching algorithms and their implementation. Caching plays a crucial role in improving the performance of systems by temporarily storing frequently accessed data, reducing the time needed to fetch the same data repeatedly from slower sources. The project focuses on understanding and implementing various cache replacement policies.

## Caching Replacement Policies Covered:

-   **FIFO (First In, First Out)**: In this policy, the first item to enter the cache is the first item to be replaced when the cache is full.
    
-   **LIFO (Last In, First Out)**: In this policy, the last item to enter the cache is the first item to be replaced when the cache is full.
    
-   **LRU (Least Recently Used)**: This policy replaces the least recently used item when the cache reaches its limit.
    
-   **MRU (Most Recently Used)**: In contrast to LRU, the MRU policy replaces the most recently used item when the cache is full.
    
-   **LFU (Least Frequently Used)**: This policy replaces the item that has been used the least often.
    

## Learning Objectives

At the end of this project, you should be able to explain, without the help of Google:

-   **What a caching system is**: 
-  caching system is a mechanism used to temporarily store frequently accessed data for faster retrieval.
-   **What FIFO means**: 
- FIFO is a cache replacement policy where the oldest cached item is replaced first.
-   **What LIFO means**: 
- LIFO is a policy where the most recently cached item is replaced first.
-   **What LRU means**: 
- LRU replaces the item that has not been used for the longest time.
-   **What MRU means**: 
- MRU replaces the most recently accessed item from the cache.
-   **What LFU means**: 
- 0LFU replaces the item that has been accessed the fewest times.
-   **What the purpose of a caching system is**: Caching is designed to speed up data retrieval and reduce load on the original data source.
-   **What limits a caching system**: Caching systems are limited by the size of the cache and the algorithms used for replacement.

## Requirements

### Python Scripts

-   All files will be executed on Ubuntu 20.04 LTS using Python 3 (version 3.9).
-   Ensure all files end with a new line.
-   The first line of every file must be `#!/usr/bin/env python3`.
-   The code should follow the pycodestyle style guide (version 2.5).
-   All files must be executable.
-   Use `wc` to test the length of your files.

### Documentation

-   Each module, class, and function must be documented with a clear explanation of its purpose and functionality.
-   Documentation should follow this format:
    -   **Module**: `python3 -c 'print(__import__("my_module").__doc__)'`
    -   **Class**: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
    -   **Function**: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`