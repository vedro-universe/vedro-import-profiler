# Vedro Import Profiler

Vedro Import Profiler allows you to profile your imports in Vedro projects, helping you identify and optimize import statements for better performance.

## Installation

To get started, you first need to install the Vedro Import Profiler plugin. Open your terminal and run the following command:

```shell
$ pip install vedro-import-profiler
```

## Enabling the Plugin Temporarily

Once installed, you can temporarily enable the Vedro Import Profiler for your current session. Additionally, you may need to disable the `assert_rewriter` plugin to avoid conflicts. Run these commands in your terminal:

```shell
$ vedro plugins enable vedro-import-profiler
$ vedro plugins disable vedro.plugins.assert_rewriter
```

## Running the Profiler

To run the profiler and generate a log of your import times, use the command below. Make sure to prepend `PYTHONPROFILEIMPORTTIME=yes` to capture the necessary data:

```shell
$ PYTHONPROFILEIMPORTTIME=yes vedro run --vedro-import-profiler 2> import.log
```

## Visualizing Import Times

After running the profiler, you can visualize the import times using the [tuna](https://github.com/nschloe/tuna) viewer. Tuna provides an intuitive interface for analyzing the performance of your imports. To use Tuna with your generated log file, execute the following command:

```shell
tuna import.log
```
