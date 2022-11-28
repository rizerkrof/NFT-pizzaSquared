// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
import { ethers } from "hardhat";

async function main() {
    let smartContractAddress = '0x1548190514fFe13D2D90fCd7501962f51b23B176'
    const Lock = await ethers.getContractFactory("Lock");
    const lock = await Lock.attach(smartContractAddress);

    let metadataBaseURI = 'https://gateway.pinata.cloud/ipfs/QmXp7uCTyEMXPwdq2dB5Lk5eUN2KFDVLMnRmXeKxraRh3x/metadata_'
    let publicKey = '0x7351968aA7d815946682d6126945CaBdE4b903A1'
    for (let i=0; i < 50; i++){
        let pizzaId = i+1
        let tokenURI = metadataBaseURI+pizzaId.toString().padStart(4, '0')+'.json'
        await lock.mintNFT(publicKey, tokenURI);
        console.log(tokenURI)
    }
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
