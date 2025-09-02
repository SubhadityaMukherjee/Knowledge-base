#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createInterface } from 'readline';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * Script to help manage art data for the gallery
 * Usage: node scripts/update-art-data.js [command]
 * 
 * Commands:
 * - scan: Scan the art_images directory and generate art-data.json
 * - add: Add a new art piece (interactive)
 * - list: List all current art pieces
 */

const ART_DATA_PATH = path.join(process.cwd(), 'content', 'art-data.json');
const ART_IMAGES_DIR = path.join(process.cwd(), 'content', 'art_images');

function loadArtData() {
  try {
    const data = fs.readFileSync(ART_DATA_PATH, 'utf-8');
    return JSON.parse(data);
  } catch (error) {
    console.log('No existing art-data.json found, starting fresh.');
    return [];
  }
}

function saveArtData(artData) {
  fs.writeFileSync(ART_DATA_PATH, JSON.stringify(artData, null, 2));
  console.log(`✅ Updated art-data.json with ${artData.length} art pieces`);
}

function scanArtImages() {
  try {
    const files = fs.readdirSync(ART_IMAGES_DIR);
    const imageFiles = files.filter(file => 
      /\.(webp|jpg|jpeg|png|gif)$/i.test(file)
    );
    
    const existingData = loadArtData();
    const existingSrcs = new Set(existingData.map(item => item.src));
    
    const newArtData = [...existingData];
    
    imageFiles.forEach(file => {
      const src = `art_images/${file}`;
      if (!existingSrcs.has(src)) {
        // Generate a title from filename
        const title = file
          .replace(/\.(webp|jpg|jpeg|png|gif)$/i, '')
          .replace(/_/g, ' ')
          .replace(/\b\w/g, l => l.toUpperCase());
        
        newArtData.push({
          src,
          alt: title,
          title: title
        });
      }
    });
    
    saveArtData(newArtData);
    console.log(`📸 Found ${imageFiles.length} images in art_images directory`);
    console.log(`➕ Added ${newArtData.length - existingData.length} new images`);
    
  } catch (error) {
    console.error('❌ Error scanning art images:', error.message);
  }
}

function listArtPieces() {
  const artData = loadArtData();
  console.log(`\n🎨 Current art pieces (${artData.length}):`);
  console.log('─'.repeat(50));
  
  artData.forEach((item, index) => {
    console.log(`${index + 1}. ${item.title}`);
    console.log(`   📁 ${item.src}`);
    console.log(`   🏷️  ${item.alt}`);
    console.log('');
  });
}

async function addArtPiece() {
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  const artData = loadArtData();
  
  rl.question('Enter image filename (e.g., my_artwork.webp): ', (filename) => {
    rl.question('Enter title: ', (title) => {
      rl.question('Enter alt text: ', (alt) => {
        const newPiece = {
          src: `art_images/${filename}`,
          title: title || filename.replace(/\.(webp|jpg|jpeg|png|gif)$/i, ''),
          alt: alt || title || filename.replace(/\.(webp|jpg|jpeg|png|gif)$/i, '')
        };
        
        artData.push(newPiece);
        saveArtData(artData);
        
        console.log('✅ Added new art piece:');
        console.log(`   Title: ${newPiece.title}`);
        console.log(`   File: ${newPiece.src}`);
        console.log(`   Alt: ${newPiece.alt}`);
        
        rl.close();
      });
    });
  });
}

// Main execution
const command = process.argv[2];

switch (command) {
  case 'scan':
    scanArtImages();
    break;
  case 'add':
    await addArtPiece();
    break;
  case 'list':
    listArtPieces();
    break;
  default:
    console.log(`
🎨 Art Data Manager

Usage: node scripts/update-art-data.js [command]

Commands:
  scan  - Scan art_images directory and auto-generate art-data.json
  add   - Add a new art piece interactively
  list  - List all current art pieces

Examples:
  node scripts/update-art-data.js scan
  node scripts/update-art-data.js add
  node scripts/update-art-data.js list
`);
    break;
}
