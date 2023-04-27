import log.log as log
from config.config import configuration
from ytworker.ytworker import *
import pandas as pd

_root_logger = log.setup_custom_logger("root")
_yt_logger_ = log.setup_custom_logger("youtube")

# Main Function
def main():
    resultPath = configuration.get_property("resultPath")
    channelIDList = configuration.get_property("channelIDList")
    channelID = ','.join(channelIDList)
    ytyoutubedata = getChannelStats(channelID)
    youtubedata = pd.DataFrame(ytyoutubedata)
    _root_logger.info(f"Displaying Multiple Youtube Channel Information.\n")
    _root_logger.info(youtubedata)

    zippedvalues = dict(zip(youtubedata["ChannelName"], youtubedata["PlaylistID"]))

    for channelName, playlistID in zippedvalues.items():
        ytvideoIDs = getVideoIDs(playlistID)
        try:
            ytvideodatadetails = getVideoDetails(ytvideoIDs)
            ytvideodata = pd.DataFrame(ytvideodatadetails)
            _root_logger.info(f'------------------------')
            _root_logger.info(f"\nDisplaying Video data for Channel: {channelName}\n")
            _root_logger.info(f'------------------------')
            _root_logger.info(f'{ytvideodata}\n')
            _root_logger.info(f"\nDisplaying Top 10 video's data for Channel: {channelName}\n")
            top10videos = ytvideodata.sort_values(by='ViewCount', ascending=False).head(10)
            _root_logger.info(f'{top10videos}')
            _root_logger.info(f'------------------------')
            ytvideodata.to_csv(f"{resultPath}VideoDetailsOf_{channelName}", index=False)
            _root_logger.info(f'File Created for {channelName}')
            _root_logger.info(f'------------------------')
        except Exception as e:
            _root_logger.error(f'Some exception occured while fetching Video data for channel {channelName}\n')

if __name__ == "__main__":
    main()
