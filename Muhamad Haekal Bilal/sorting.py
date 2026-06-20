import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import copy
import sys

sys.setrecursionlimit(100000)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)

st.title("Sorting Algorithm Benchmark")

if st.button("Jalankan Benchmark"):
    data_sizes = [100, 1000, 10000, 50000]
    algorithms = {
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }

    results = {algo: [] for algo in algorithms}
    
    progress_text = st.empty()

    for size in data_sizes:
        progress_text.write(f"Sedang melakukan benchmark untuk ukuran data: {size}...")
        base_data = [random.randint(1, 100000) for _ in range(size)]
        
        for algo_name, algo_func in algorithms.items():
            times = []
            for _ in range(3):
                data_copy = copy.deepcopy(base_data)
                
                start_time = time.time()
                algo_func(data_copy)
                end_time = time.time()
                
                times.append(end_time - start_time)
            
            avg_time = sum(times) / 3
            results[algo_name].append(avg_time)
            
    progress_text.write("Benchmark selesai!")

    df_results = pd.DataFrame(results, index=data_sizes)
    df_results.index.name = 'Data Size'
    
    st.subheader("Tabel Hasil Benchmarking (detik)")
    st.dataframe(df_results)

    st.subheader("Visualisasi Grafik")
    fig, ax = plt.subplots(figsize=(10, 6))
    for algo_name in algorithms:
        ax.plot(data_sizes, results[algo_name], marker='o', label=algo_name)

    ax.set_title('Sorting Algorithm Benchmark')
    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Average Execution Time (Seconds)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)