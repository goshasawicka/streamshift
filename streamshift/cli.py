#!/usr/bin/env python

from multiprocessing import Process
from streamshift import StreamProcess, app

import ConfigParser
import click


@click.command()
@click.option('--mode', default="empty",
              help="Type 'web' for streaming audio or 'buffer' to start buffering data")
def cli(mode):
    """Buffer audio data and stream it with user-defined offset"""
    if mode == 'buffer':
        config = ConfigParser.ConfigParser()
        config.read('./config.cfg')

        stations = config.sections()
        stations.remove('global')
        for station in stations:

            config_setup = config.items(station)

            config_setup.append(("path", config.items("global")[0][1]))
            cp = StreamProcess(config_setup)
            for f in [cp.purge, cp.buffering]:
                Process(target=f).start()

    elif mode == 'web':
        config = ConfigParser.ConfigParser()
        config.read('./config.cfg')

        stations = config.sections()
        stations.remove('global')
        urls = {}
        for station in stations:
            urls[station] = config.get(station, 'url')

        app.config['URLS'] = urls
        app.run(host="0.0.0.0", port=config.items(config.sections()[0])[1][1], threaded=True)

    else:
        click.echo("UUUPS: Incorrect mode. Please refer to --help for assistance")

if __name__ == '__main__':
    cli()
