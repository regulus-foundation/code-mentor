import Bytes from "../utils/bytes";
import PrvKey from "../crypto/secp256k1/prvKey";
import PubKey from "../crypto/secp256k1/pubKey";
import BN from 'bn.js'

export default class Account {
    address: string
    name: string
    nonce: number
    balance: string
    #prvKey: PrvKey
    #pubKey: PubKey

    // Create new account
    static New(nm: string, secret: string): Account {
        const ret = new Account()
        ret.name = nm
        ret.nonce = 0
        ret.balance = "0"
        ret.#prvKey = new PrvKey()
        ret.#pubKey = new PubKey(ret.#prvKey)
        ret.address = ret.#pubKey.toAddress().toHex()
        return ret
    }

    // Import existing account
    static Import(nm: string, secret: string, d: Bytes, dsecret?:string): Account {
        const ret = new Account()
        ret.name = nm
        ret.nonce = 0
        ret.balance = "0"
        if(dsecret) {
            // todo: if `dsecret` has value, `d` is not plaintext and should be decrypted.
        }
        ret.#prvKey = PrvKey.import(d)
        ret.#pubKey = new PubKey(ret.#prvKey)
        ret.address = ret.#pubKey.toAddress().toHex()
        return ret
    }

    // Unmarshal account
    static Unmarshal(bz: string): Account {
        const ret = new Account()
        ret.unmarshal(bz)
        return ret
    }

    // Update account information
    update(obj: {address:string, nonce:number, balance:string}) {
        if(this.address.toLowerCase() !== obj.address.toLowerCase()) {
            console.error(`this address: ${this.address}`)
            console.error(`param's address: ${obj.address}`)
            throw Error('the address is not same')
        }
        this.nonce = obj.nonce
        this.balance = obj.balance
    }

    // Lock account
    lock() {
        return
    }

    // Unlock account
    unlock(s?: string): boolean {
        return true
    }

    // Increase account balance
    addBalance(amt: string) {
        const _bal = new BN(this.balance).add(new BN(amt))
        this.balance = _bal.toString(10)
    }

    // Sign message
    sign(msg: Uint8Array): Bytes {
        const sigobj = this.#prvKey.sign(msg)
        return new Bytes([...sigobj.signature, (sigobj.recid & 0xff)])
    }

    // Verify message
    verify(sig: Uint8Array, msg: Uint8Array): boolean {
        return this.#pubKey.verify(sig, msg)
    }

    // Export account
    export(secret: string): Bytes {
        return this.#prvKey.export()
    }

    // Marshal account
    marshal():string {
        let tmp = {
            address: this.address,
            name: this.name,
            nonce: this.nonce,
            balance: this.balance,
            prvKey: this.#prvKey.export().toHex(),
            pubKey: new Bytes([...this.#pubKey.x, ...this.#pubKey.y]).toHex()
        }
        return JSON.stringify(tmp)
    }

    // Unmarshal account
    unmarshal(bz: string) {
        const tmp = JSON.parse(bz)
        this.address = tmp.address
        this.name = tmp.name
        this.nonce = tmp.nonce
        this.balance = tmp.balance
        this.#prvKey = PrvKey.import(tmp.prvKey)
        this.#pubKey = new PubKey(this.#prvKey)

        if (this.address.toLowerCase() !== this.#pubKey.toAddress().toHex().toLowerCase()) {
            console.error(`address: ${this.address}`)
            console.error(`public key: ${this.#pubKey.toAddress().toHex()}`)
            throw Error("the address is not driven from the public key")
        }
    }
}