class PCG {
  var state: UInt64
  let seed: UInt64

  init() {
    state = 0
    seed = 1
  }

  init(_ s: Int) {
    state = 0
    seed = UInt64(s) * 2 + 1
  }

  func Next() -> UInt32 {
    defer {
      // Advance internal state
      (state, _) = UInt64.multiplyWithOverflow(state, UInt64(6364136223846793005))
      (state, _) = UInt64.addWithOverflow(state, seed)
    }

    // Calculate output function (XSH RR), uses old state for max ILP
    let xorshifted = UInt32(((state >> UInt64(18)) ^ state) >> UInt64(27) & UInt64(UInt32.max))
    let rot = UInt32(state >> UInt64(59))
    let lrot = ~rot & UInt32(31)

    return (xorshifted >> rot) | (xorshifted << lrot);
  }

  func UniformImpl(_ n: UInt32) -> UInt32 {
    let m = (UInt32.max / n) * n

    while true {
      let r = Next()

      if r < m {
        return r % n
      }
    }
  }

  func Uniform(_ n: Int) -> Int {
    return Int(UniformImpl(UInt32(n)))
  }

  static func Enumerate(_ seed: Int) -> AnyIterator<Int> {
    let rng = PCG(seed)

    return AnyIterator {
      return Int(rng.Next())
    }
  }
}

fileprivate let MAP = [
  "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
  "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
  "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
  "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]

func F84() -> Int {
  let gen = PCG()
  var pos = 0
  var prob = [String: Int]()
  var bylab = [String: Int]()
  var cc = ["GO", "JAIL"] + (1...14).map{_ in ""}
  var ch = ["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", "3"] + (1...6).map{_ in ""}

  for (n, x) in MAP.enumerated() {
    bylab[x] = n
  }

  func Throw() -> Int {
    return 2 + gen.Uniform(4) + gen.Uniform(4)
  }

  func Find(_ x: String) -> Int {
    return bylab[x]!
  }

  func FindNext(_ x: String) -> Int {
    var c = pos + 1

    while true {
      let cc = c % MAP.count

      if MAP[cc].characters.first! == x.characters.first! {
        return cc
      }

      c += 1
    }
  }

  func CH() -> String {
    let res = ch.popLast()!

    ch = [res] + ch

    return res
  }

  func CC() -> String {
    let res = cc.popLast()!

    cc = [res] + cc

    return res
  }

  let jail = Find("JAIL")

  func SetPos(_ n: Int) {
    pos = n

    let lab = MAP[n]

    if lab == "G2J" {
      SetPos(jail)

      return
    }

    if lab == "CH1" || lab == "CH2" || lab == "CH3" {
      let code = CH()

      if code.characters.count > 0 {
        if code.characters.count == 1 {
          if code == "3" {
            IncPos(37)
          } else {
            SetPos(FindNext(code))
          }
        } else {
          SetPos(Find(code))
        }
      }

      return
    }

    if lab == "CC1" || lab == "CC2" || lab == "CC3" {
      let code = CC()

      if code.characters.count > 0 {
        SetPos(Find(code))
      }

      return
    }

    let k = MAP[n]

    if prob[k] == nil {
      prob[k] = 1
    } else {
      prob[k]! += 1
    }
  }

  func IncPos(_ n: Int) {
    SetPos((pos + n) % MAP.count)
  }

  for _ in 1...1000000 {
    IncPos(Throw())
  }

  for (k, v) in prob.sorted(by: {$0.1 > $1.1})[0...2] {
    print(Find(k), v)
  }

  return 0
}

print(F84())
