#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * Script to parse art information from your existing My Art.md file
 * and generate art-data.json automatically
 */

const MARKDOWN_PATH = path.join(process.cwd(), 'content', 'My Art.md');
const ART_DATA_PATH = path.join(process.cwd(), 'content', 'art-data.json');
const ART_DATA_TS_PATH = path.join(process.cwd(), 'quartz', 'data', 'artData.ts');

function parseArtFromMarkdown() {
  try {
    const markdownContent = fs.readFileSync(MARKDOWN_PATH, 'utf-8');
    
    // Regular expression to match art entries in the markdown
    // Matches patterns like: "- Description ![[image.webp]]"
    const artRegex = /^-\s*(.+?)\s*!\[\[([^\]]+)\]\]/gm;
    
    const artPieces = [];
    let match;
    
    while ((match = artRegex.exec(markdownContent)) !== null) {
      const description = match[1].trim();
      const imageFile = match[2].trim();
      
      // Skip if it's not an art image (contains common non-art patterns)
      if (description.toLowerCase().includes('faq') || 
          description.toLowerCase().includes('software') ||
          description.toLowerCase().includes('brushes') ||
          description.toLowerCase().includes('gouache')) {
        continue;
      }
      
      artPieces.push({
        src: `art_images/${imageFile}`,
        alt: description,
        title: description
      });
    }
    
    // Save the parsed data
    fs.writeFileSync(ART_DATA_PATH, JSON.stringify(artPieces, null, 2));
    
    // Generate TypeScript file
    const tsContent = `export interface ArtImage {
  src: string
  alt: string
  title?: string
}

export const artImages: ArtImage[] = ${JSON.stringify(artPieces, null, 2)}
`;
    
    fs.writeFileSync(ART_DATA_TS_PATH, tsContent);
    
    console.log(`✅ Parsed ${artPieces.length} art pieces from My Art.md`);
    console.log(`📝 Generated art-data.json and artData.ts`);
    
    // Show a preview
    console.log('\n🎨 Preview of parsed art pieces:');
    artPieces.slice(0, 5).forEach((piece, index) => {
      console.log(`${index + 1}. ${piece.title}`);
      console.log(`   📁 ${piece.src}`);
    });
    
    if (artPieces.length > 5) {
      console.log(`   ... and ${artPieces.length - 5} more`);
    }
    
  } catch (error) {
    console.error('❌ Error parsing markdown:', error.message);
  }
}

// Run the parser
parseArtFromMarkdown();
