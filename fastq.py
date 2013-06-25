import itertools


__version__ = '0.1'


class Fastq(object):

    def __init__(self, header, sequence, quality):
        self.header = header
        self.sequence = sequence
        self.quality = quality

    def __str__(self):
        fmt = '@{}\n{}\n+\n{}'
        return fmt.format(self.header, self.sequence, self.quality)


class Reader(object):
    Fastq = Fastq

    def __init__(self, stream):
        self.stream = stream

    def __iter__(self):
        return self

    def next(self):
        header = self.stream.next().strip()
        # Strip the leading '@'
        header = header[1:]
        sequence = self.stream.next().strip()
        # Ignore the line that separates sequence from quality.
        # Why does this even exist?
        _ = self.stream.next()
        quality = self.stream.next().strip()
        return self.Fastq(header, sequence, quality)


class PairedReader(object):
    Reader = Reader

    def __init__(self, mate_1, mate_2):
        self.mate_1_reader = self.Reader(mate_1)
        self.mate_2_reader = self.Reader(mate_2)
        self.reader = itertools.izip(self.mate_1_reader, self.mate_2_reader)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next()
