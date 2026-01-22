from dataclasses import dataclass
from typing import Literal, Optional
from enum import StrEnum
from Sequences import NucleotideSequence, DNASequence, RNASequence, ProteinSequence
from abc import ABC, abstractmethod

class SeqKind(StrEnum):
    DNA = 'DNA'
    RNA = 'RNA'
    Protein = 'Protein'


@dataclass(frozen=True, slots=True)
class SeqStats:
    id: str
    kind: SeqKind
    length: int
    gc_fraction: Optional[float] = None

    @classmethod
    def summarise(cls, sequence: NucleotideSequence | ProteinSequence) -> 'SeqStats': #it doesnt know Seqstats exists yet so must use quotes and it will resolve it later
        if isinstance(sequence, DNASequence):
            return cls(sequence.id, SeqKind.DNA, len(sequence), sequence.calc_gc_content())
        if isinstance(sequence, RNASequence):
            return cls(sequence.id, SeqKind.RNA, len(sequence), sequence.calc_gc_content())
        if isinstance(sequence, ProteinSequence):
            return cls(sequence.id, SeqKind.Protein, len(sequence))
        raise ValueError(f'Error, SeqKind is neither RNA or DNA')