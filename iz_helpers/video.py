import numpy as np
import imageio
from PIL import Image

def write_video(file_path, frames, fps, reversed=True, start_frame_dupe_amount=15, last_frame_dupe_amount=30):
    """
    Writes frames to an mp4 video file
    :param file_path: Path to output video, must end with .mp4
    :param frames: List of PIL.Image objects
    :param fps: Desired frame rate
    :param reversed: if order of images to be reversed (default = True)
    """
    if reversed == True:
        frames = frames[::-1]

    # Drop missformed frames
    frames = [frame for frame in frames if frame.size == frames[0].size]

    # Create an imageio video writer, avoid block size of 512.
    writer = imageio.get_writer(file_path, fps=fps, macro_block_size=None)

    # Duplicate the start and end frames
    start_frames = [frames[0]] * start_frame_dupe_amount
    end_frames = [frames[-1]] * last_frame_dupe_amount

    # Write the duplicated frames to the video writer
    for frame in start_frames:
        # Convert PIL image to numpy array
        np_frame = np.array(frame)
        writer.append_data(np_frame)

    # Write the frames to the video writer
    for frame in frames:
        np_frame = np.array(frame)
        writer.append_data(np_frame)

    # Write the duplicated frames to the video writer
    for frame in end_frames:
        np_frame = np.array(frame)
        writer.append_data(np_frame)

    # Close the video writer
    writer.close()
    

class ContinuousVideoWriter:

    _writer = None
    
    def __init__(self, file_path, initframe, fps, start_frame_dupe_amount=15):
        """
        Writes initial frame to a new mp4 video file
        :param file_path: Path to output video, must end with .mp4
        :param frame: Start image PIL.Image objects
        :param fps: Desired frame rate
        :param reversed: if order of images to be reversed (default = True)
        """

        writer = imageio.get_writer(file_path, fps=fps, macro_block_size=None)
        start_frames = [initframe] * start_frame_dupe_amount
        for f in start_frames:
            writer.append_data(np.array(f))
        self._writer = writer
    
    def append(self, frames):
        """
        Append a list of image PIL.Image objects to the end of the file.
        :param frames: List of image PIL.Image objects
        """
        for i,f in enumerate(frames):
            self._writer.append_data(np.array(f))
    
    def finish(self, frame, last_frame_dupe_amount=30 ):
        """
        Closes the file writer.
        """
        for i in range(last_frame_dupe_amount):
            self._writer.append_data(np.array(frame))
        
        self._writer.close()
    