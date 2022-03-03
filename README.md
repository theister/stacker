# pinless-stacker

.. image:: https://readthedocs.org/projects/stacker/badge/?version=latest
   :target: http://stacker.readthedocs.org/en/latest/


"pinless-stacker" is a fork of [stacker](https://github.com/cloudtools/stacker).

For full usage documentation, please see the original stacker 1.7.2 documentation on [readthedocs](https://stacker.readthedocs.io/en/stable/).

## About

stacker is a tool and library used to create & update multiple CloudFormation
stacks. It was originally written at Remind_ and
released to the open source community.

stacker Blueprints are written in troposphere_, though the purpose of
most templates is to keep them as generic as possible and then use
configuration to modify them.

The original stacker is no longer maintained and is EOL.

`pinless-stacker` has been forked off stacker at release 1.7.2.

It removes python 2 support, which allows removing upper bounds of the dependency ranges that make integration into modern python environments hard.
It supports troposphere 3.*

## Requirements

* Python 3.7+

## Stacker Command

The ``stacker`` command has sub-commands, similar to git.

Here are some examples:

  ``build``:
    handles taking your stack config and then launching or updating stacks as necessary.

  ``destroy``:
    tears down your stacks

  ``diff``:
    compares your currently deployed stack templates to your config files

  ``info``:
    prints information about your currently deployed stacks

We document these sub-commands in full along with others, in the documentation.


## Getting Started

Don't use stacker for any new project.
This is a fork meant to prolong the live of stacker a little and to ease migration away from it.

There is no guarantee for further support.


## Building a wheel:
