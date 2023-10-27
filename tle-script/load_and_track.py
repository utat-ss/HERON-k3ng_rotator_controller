import logging
from argparse import ArgumentParser

from k3ng import K3NG, Satellite


def program_tle(sat_id: int, ser_port: str, track: bool) -> None:
    rot = K3NG(ser_port)

    sat = Satellite(sat_id)
    rot.set_time()
    rot.load_tle(sat)
    rot.check_time()
    rot.select_satellite(sat)
    rot.enable_tracking()
    rot.get_tracking_status()


def main():
    parser = ArgumentParser(
        prog="load_and_track.py",
        description="Loads a TLE and begins tracking it"
    )
    parser.add_argument(
        "port",
        help="Serial port connected to an Arduino (typically /dev/ttyACM0)",
    )
    parser.add_argument(
        "norad_id",
        type=int,
        help="NORAD ID of a satellite, (ex. use 25544 for the ISS)",
    )

    logging.basicConfig(level=logging.DEBUG)

    args = parser.parse_args()

    program_tle(args.norad_id, args.port, False)


if __name__ == "__main__":
    main()
