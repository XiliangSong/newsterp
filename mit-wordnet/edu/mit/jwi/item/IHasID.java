/******************************************************************************
 * Copyright (c) 2007 Mark Alan Finlayson
 * 
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the MIT Java Wordnet Interface 
 * Public License v1.0 which accompanies this distribution, and is 
 * available at http://www.mit.edu/~markaf/projects/wordnet/license.html.
 *****************************************************************************/

package edu.mit.jwi.item;

/** Indicates that the implementing object has an ID object of type T, which is 
 * returned by the call.
 * @author Mark A. Finlayson
 * @version 1.00, Apr 20, 2007
 * @since 1.5.0
 */
public interface IHasID<T extends IItemID> {
    
    /** Returns the ID object.
     * @return T  The ID object
     */
    public T getID();

}
