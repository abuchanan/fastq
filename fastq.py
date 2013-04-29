class Fastq(object):

    def __init__(self, header, sequence, quality):
        self.header = header
        self.sequence = sequence
        self.quality = quality

    def __str__(self):
        fmt = '@{}\n{}\n+\n{}'
        return fmt.format(self.header, self.sequence, self.quality)


def reader(stream):
    while True:
        header = stream.next().strip()
        # Strip the leading '@'
        header = header[1:]
        sequence = stream.next().strip()
        # Ignore the line that separates sequence from quality.
        # Why does this even exist?
        _ = stream.next()
        quality = stream.next().strip()
        yield Fastq(header, sequence, quality)
